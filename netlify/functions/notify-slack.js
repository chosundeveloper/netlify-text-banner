const DEFAULT_HEADERS = {
  'Content-Type': 'application/json',
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Allow-Methods': 'POST,OPTIONS',
};

const respond = (statusCode, payload) => ({
  statusCode,
  headers: DEFAULT_HEADERS,
  body: JSON.stringify(payload),
});

exports.handler = async (event) => {
  if (event.httpMethod === 'OPTIONS') {
    return respond(200, { ok: true });
  }

  if (event.httpMethod !== 'POST') {
    return respond(405, { error: 'Method Not Allowed' });
  }

  const webhookUrl = process.env.SLACK_WEBHOOK_URL;
  if (!webhookUrl) {
    console.error('Slack webhook URL is not configured');
    return respond(500, { error: 'Slack webhook not configured' });
  }

  let payload;
  try {
    payload = JSON.parse(event.body || '{}');
  } catch (error) {
    console.warn('Invalid JSON payload', error);
    return respond(400, { error: 'Invalid JSON' });
  }

  const { title, src, author } = payload;
  const messageLines = [
    '🎞️ 동영상이 업로드되었습니다.',
    title ? `제목: ${title}` : null,
    author ? `업로더: ${author}` : null,
    src ? `링크: ${src}` : null,
  ].filter(Boolean);

  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: messageLines.join('\n') }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Slack webhook error:', response.status, errorText);
      return respond(502, { error: 'Slack notification failed' });
    }
  } catch (error) {
    console.error('Slack webhook request failed', error);
    return respond(502, { error: 'Slack notification failed' });
  }

  return respond(200, { ok: true });
};
