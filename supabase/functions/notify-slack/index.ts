import { serve } from "https://deno.land/std@0.224.0/http/server.ts";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

const SLACK_WEBHOOK_URL = Deno.env.get("SLACK_WEBHOOK_URL") ?? "";

const sendSlackNotification = async (payload: { title?: string; src?: string; author?: string }) => {
  if (!SLACK_WEBHOOK_URL) {
    console.error("SLACK_WEBHOOK_URL is not configured");
    throw new Error("Slack webhook not configured");
  }

  const messageLines = [
    "🎞️ 동영상이 업로드되었습니다.",
    payload.title ? `제목: ${payload.title}` : null,
    payload.author ? `업로더: ${payload.author}` : null,
    payload.src ? `링크: ${payload.src}` : null,
  ].filter(Boolean);

  const response = await fetch(SLACK_WEBHOOK_URL, {
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
