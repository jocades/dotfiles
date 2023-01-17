local M = {}

M.treesitter = {
  ensure_installed = {
    "vim",
    "lua",
    "typescript",
    "javascript",
    "tsx",
    "python",
    "html",
    "css",
  },
  rainbow = {
    enable = true,
    extended_mode = false,
    max_file_lines = nil,
  },
}

M.mason = {
  ensure_installed = {
    -- lua stuff
    "lua-language-server",
    "stylua",

    -- web dev
    "css-lsp",
    "html-lsp",
    "typescript-language-server",
    "json-lsp",

    -- python
    "pyright",
    "autopep8",

    -- shell
    "shfmt",
    "shellcheck",
  },
}

-- Change the order in pop-up menu.
M.cmp = {
  sources = {
    { name = "nvim_lsp" },
    { name = "buffer" },
    { name = "nvim_lua" },
    { name = "luasnip" },
    { name = "path" },
  },
}

-- git support in nvimtree
M.nvimtree = {
  git = {
    enable = true,
  },

  renderer = {
    highlight_git = true,
    icons = {
      show = {
        git = true,
      },
    },
  },
}

return M
