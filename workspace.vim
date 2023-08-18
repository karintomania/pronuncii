function! RunFormatCommand()
  " Run black command
  execute "!black %"
  " Run pylint command
  execute "!pylint %"
endfunction
" Map the function to the :Format command
command! -nargs=0 Format call RunFormatCommand()

function! RunCurrentTest()
  " Get the current file path
  let l:filename = expand('%:p')
  " Extract the Django app and test module names from the file path
  let l:parts = split(l:filename, '/')
  let l:app_name = substitute(l:parts[-3], '\\.', ' ', 'g')
  let l:module_name = substitute(l:parts[-1], '\\.py$', '', '')
  " Construct the command to run the test
  let l:command = 'docker exec pronuncii-py python manage.py test ' . l:app_name . '.' . l:module_name
  " Open a terminal window and run the command
  execute "belowright split|terminal " . l:command
endfunction
" Bind the RunCurrentTest function to the :RunCurrentTest command
command! -nargs=0 RunCurrentTest call RunCurrentTest()