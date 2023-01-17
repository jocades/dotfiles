local M = {}

M.general = {
  i = {
    ["jk"] = { "<ESC>", "escape insert mode", opts = { nowait = true } },
  },

  n = {
    ["<leader>s"] = { "<cmd> vsplit <CR>" },
  },
}

return M
