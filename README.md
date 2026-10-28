# LogRocket plugin for ChatGPT and Codex

Connect ChatGPT and Codex to [LogRocket](https://logrocket.com) to investigate session replays, network requests, issues, and product analytics. The plugin uses the [Agent Plugins 1.0](https://agent-plugins.org) format, connects to LogRocket's hosted MCP server, and includes a skill that guides the agent through LogRocket investigations.

## Layout

- `plugins/logrocket/`: the self-contained plugin (`plugin.json`, `mcp.json`, skill, logo, and usage documentation). See its [README](plugins/logrocket/README.md) for connection options.
- `.agents/plugins/marketplace.json`: a repository marketplace pointing to the plugin.
- `scripts/package.py`: a dependency-free ZIP builder for the plugin.
- `docs/testing.md`: manual test cases for a connected plugin.

## Install locally

From the repository root, register it as a marketplace:

```sh
codex plugin marketplace add .
```

Open the app's Plugins directory, select **LogRocket Plugins**, and install **LogRocket**. Reload the app if the marketplace is not visible. Complete LogRocket OAuth through the connection flow, then test in a new chat. Host support for local marketplaces can vary; see the [OpenAI plugin guide](https://developers.openai.com/plugins/build/plugins).

## Package

Run with Python 3.9 or later from the repository root:

```sh
python3 scripts/package.py
```

This creates `dist/logrocket-<version>.zip` containing only the plugin files and license, with manifests at the archive root. The version comes from `plugins/logrocket/plugin.json`. Pass an output path as the first argument to write the archive elsewhere.

## Development

Edit files in `plugins/logrocket/`, bump `version` in `plugins/logrocket/plugin.json` for releases, rebuild, and reinstall or refresh the plugin through the host. The skill describes tool behavior but does not freeze tool input schemas; the agent discovers current schemas from the server at runtime.

References:

- [LogRocket MCP documentation](https://docs.logrocket.com/docs/mcp)
- [OpenAI plugin guide](https://developers.openai.com/plugins/build/plugins)

## License

The code and documentation in this repository are available under the [MIT License](LICENSE). The LogRocket name and logo are trademarks of LogRocket, Inc. and are not licensed under the MIT License.
