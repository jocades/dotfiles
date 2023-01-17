local overrides = require "custom.plugins.overrides"

return {

  ["goolord/alpha-nvim"] = { disable = false }, -- enables dashboard

  -- Override plugin definition options
  ["neovim/nvim-lspconfig"] = {
    config = function()
      require "plugins.configs.lspconfig"
      require "custom.plugins.lspconfig"
    end,
  },

  -- override plugin configs
  ["nvim-treesitter/nvim-treesitter"] = {
    override_options = overrides.treesitter,
  },

  ["hrsh7th/nvim-cmp"] = {
    override_options = overrides.cmp, -- change order of sources in popup window, 1st = lsp, 2nd = buffer
  },

  ["williamboman/mason.nvim"] = {
    override_options = overrides.mason,
  },

  ["kyazdani42/nvim-tree.lua"] = {
    override_options = overrides.nvimtree,
  },

  -- Install plugin
  ["jose-elias-alvarez/null-ls.nvim"] = {
    after = "nvim-lspconfig",
    config = function()
      require "custom.plugins.null-ls"
    end,
  },

  -- Colored parentheses, brackets, etc.
  ["p00f/nvim-ts-rainbow"] = {},

  -- remove plugitruen
  -- ["hrsh7th/cmp-path"] = false,

  -- ["lukas-reineke/indent-blankline.nvim"] = false,
}
