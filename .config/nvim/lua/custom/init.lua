vim.cmd "set rnu"
vim.cmd "set nowrap"

vim.opt.fillchars = { eob = "~" }
vim.wo.cursorline = true

-- Change neovim nvchad copilot keybinds
-- If you'd rather use a key that isn't <Tab>, define an <expr> map that calls
-- copilot#Accept().  Here's an example with CTRL-J:
-- >
--         imap <silent><script><expr> <C-J> copilot#Accept("\<CR>")
--         let g:copilot_no_tab_map = v:true
-- How to to this in lua?

-- vim.g.copilot_assume_mapped = true
-- vim.g.copilot_no_tab_map = true
-- vim.keymap.set("i", "<C-J>", "<Plug>(copilot-accept)", { silent = true, expr = true })
