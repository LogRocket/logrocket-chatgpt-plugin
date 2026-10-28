# LogRocket

Connect ChatGPT and Codex to the hosted LogRocket MCP server for session replay investigations, network debugging, issue triage, and product analytics.

The plugin connects to `https://mcp.logrocket.com/mcp` over Streamable HTTP. The server advertises OAuth through its standard authentication challenge and discovery endpoints; use the host's OAuth connection flow. The MCP declaration uses only the portable schema fields and leaves OAuth endpoint discovery to the host. No API key, client secret, local server, or Node dependency is included. OAuth grants access to the same organizations and projects available to the signed-in user.

The bundled `use-logrocket` skill routes requests to the available tools and handles project discovery, asynchronous analysis, timezone-aware queries, pagination, and evidence citations. Available tools depend on server deployment and connection scope.

Try:

- “Find sessions for this user from yesterday and investigate their checkout problem.”
- “Show severe untriaged issues from the last week and prioritize them by impact.”
- “Analyze this saved funnel metric over the last seven days and investigate example drop-offs.”
- “Inspect failed network requests in this LogRocket session.”

## Connection options

Edit the server URL in `mcp.json` before installing a customized copy:

- Organization scope: `https://mcp.logrocket.com/mcp/<organizationID>`
- Project scope: `https://mcp.logrocket.com/mcp/<organizationID>/<projectID>`
- Toolsets: `?toolsets=sessions,metrics` (supported: `sessions`, `metrics`, `issues`, `ask-galileo`, `all`)
- Default metric timezone: `?timezone=America/New_York`
- Combined: `?toolsets=sessions,metrics&timezone=America/New_York`

The default package leaves all tools available and does not set a timezone. Scoped connections hide unneeded discovery tools. Toolset restrictions limit exposed tools; they do not replace server authorization.

OAuth is the default. LogRocket also supports project-scoped API keys for clients that need them; use the client's secret/environment configuration rather than committing credentials. For a standalone Codex connection using an API key, the documented command is:

```sh
codex mcp add logrocket --url https://mcp.logrocket.com/mcp --bearer-token-env-var LOGROCKET_API_KEY
```

Set `LOGROCKET_API_KEY` outside this package. This standalone connection is an alternative to the plugin connection, and adding both can expose duplicate tools.

See [LogRocket MCP documentation](https://docs.logrocket.com/docs/mcp) for current setup details.

## License

MIT, except for the LogRocket name and logo, which are trademarks of LogRocket, Inc.
