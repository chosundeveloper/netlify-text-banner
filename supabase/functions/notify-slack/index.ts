import { serve } from "https://deno.land/std@0.224.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

const SUPABASE_URL = Deno.env.get("SUPABASE_URL") ?? "";
const SUPABASE_SERVICE_ROLE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? "";
const SETTINGS_TABLE = Deno.env.get("SLACK_SETTINGS_TABLE") ?? "app_settings";
const SETTINGS_KEY = Deno.env.get("SLACK_SETTINGS_KEY") ?? "slack_webhook_url";

const getSlackWebhookUrl = async () => {
  if (!SUPABASE_URL || !SUPABASE_SERVICE_ROLE_KEY) {
    console.error("Supabase service role credentials are not configured");
    throw new Error("Supabase service role not configured");
  }

  const supabaseAdmin = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, {
    auth: { persistSession: false },
  });

  const { data, error } = await supabaseAdmin
    .from(SETTINGS_TABLE)
    .select("value")
    .eq("key", SETTINGS_KEY)
    .maybeSingle();

  if (error) {
    console.error("Failed to load Slack webhook URL", error);
    throw new Error("Unable to load Slack webhook URL");
  }

  const value = data?.value ?? "";
  if (!value) {
    throw new Error("Slack webhook URL is missing in settings table");
  }

  return value as string;
};

const sendSlackNotification = async (payload: { title?: string; src?: string; author?: string }) => {
  const webhookUrl = await getSlackWebhookUrl();

  const messageLines = [
    "🎞️ 동영상이 업로드되었습니다.",
    payload.title ? `제목: ${payload.title}` : null,
    payload.author ? `업로더: ${payload.author}` : null,
    payload.src ? `링크: ${payload.src}` : null,
  ].filter(Boolean);

  const response = await fetch(webhookUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: messageLines.join("\n") }),
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Slack webhook error: ${response.status} ${errorText}`);
  }
};

serve(async (req) => {
  if (req.method === "OPTIONS") {
    return new Response(JSON.stringify({ ok: true }), {
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  }

  if (req.method !== "POST") {
    return new Response(JSON.stringify({ error: "Method Not Allowed" }), {
      status: 405,
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  }

  let payload: { title?: string; src?: string; author?: string } = {};
  try {
    payload = await req.json();
  } catch (error) {
    return new Response(JSON.stringify({ error: "Invalid JSON" }), {
      status: 400,
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  }

  try {
    await sendSlackNotification(payload);
    return new Response(JSON.stringify({ ok: true }), {
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  } catch (error) {
    console.error("Failed to notify Slack", error);
    return new Response(JSON.stringify({ error: error.message ?? "Slack notification failed" }), {
      status: 502,
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  }
});
