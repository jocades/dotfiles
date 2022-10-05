local present, null_ls = pcall(require, "null-ls")
local augroup = vim.api.nvim_create

if not present then
  return
end

local b = null_ls.builtins

local sources = {

  -- Javascript
  b.formatting.prettier.with { extra_args = { "--no-semi" } },

  -- Python
  b.formatting.autopep8,

  -- Lua
  b.formatting.stylua,

  -- Shell
  b.formatting.shfmt,
  b.diagnostics.shellcheck.with { diagnostics_format = "#{m} [#{c}]" },
}

null_ls.setup {
  debug = true,
  sources = sources,

  -- format on save
  on_attach = function(client)
    if client.resolved_capabilities.document_formatting then
      vim.cmd "autocmd BufWritePre <buffer> lua vim.lsp.buf.formatting_sync()"
    end
  end,
}
