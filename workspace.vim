lua << EOF
EOF

function! RunFormatCommand()
  " Run black command
  execute "!black %"
  " Run pylint command
  execute "belowright split|terminal pylint %"
endfunction
" Map the function to the :Format command
command! -nargs=0 Format call RunFormatCommand()

function! TestPython()
  " Get the current file path
  let l:current_file = expand('%')
  let l:filepath = fnamemodify(l:current_file, ':~:.')
  " Extract the Django app and test module names from the file path
  let l:filepath = substitute(l:filepath, '/', '.', 'g')
  let l:filepath = substitute(l:filepath, '.py$', '', '')
  let l:filepath = substitute(l:filepath, '^src.', '', '')
  " Construct the command to run the test
  let l:command = 'docker exec pronuncii-py python manage.py test ' . l:filepath

  " Open a terminal window and run the command
  execute "belowright split|terminal " . l:command
endfunction

" Bind the RunCurrentTest function to the :RunCurrentTest command
command! -nargs=0 TestPython call TestPython()
