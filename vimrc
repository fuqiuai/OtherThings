set nocompatible              " required
filetype off                  " required
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'gmarik/Vundle.vim'
Plugin 'scrooloose/nerdtree' "列出当前路径的目录数，快捷键<F2>
Plugin 'scrooloose/nerdcommenter' "快速注释插件，默认快捷键 注释‘\cc’ 解注释‘\cu’
Plugin 'majutsushi/tagbar' "显示文件的类变量等数据，快捷键<F8>
Plugin 'Lokaltog/vim-powerline' "增强状态栏插件
Plugin 'vim-scripts/indentpython.vim' "自动缩进插件
" Plugin 'scrooloose/syntastic' "每次保存文件时Vim都会检查代码的语法
Plugin 'Valloric/YouCompleteMe' "自动补全插件
Plugin 'godlygeek/tabular' "markdown语法高亮插件
Plugin 'plasticboy/vim-markdown'
Plugin 'andviro/flake8-vim' "语法检查插件

call vundle#end()            " required
filetype plugin indent on    " required

"nerdcommenter插件配置
" 注释的时候自动加个空格, 强迫症必配
" let g:NERDSpaceDelims=1

"powerline插件配置
set guifont=PowerlineSymbols\ for\ Powerline
set nocompatible
set t_Co=256
let g:Powerline_symbols = 'fancy'

"tagbar插件配置
"设置tagbar使用的ctags的插件,必须要设置对  
let g:tagbar_ctags_bin='/usr/bin/ctags'  
"设置tagbar的窗口宽度  
let g:tagbar_width=30  
"设置tagbar的窗口显示的位置,为左边  
let g:tagbar_right=1  
"打开文件自动 打开tagbar  
autocmd BufReadPost *.cpp,*.c,*.h,*.hpp,*.cc,*.cxx call tagbar#autoopen()  
"映射tagbar的快捷键  
map <F8> :TagbarToggle<CR> 

"nerdtree插件配置
"使用F2键快速调出和隐藏它
map <F2> :NERDTreeToggle<CR>
"关闭vim时，如果打开的文件除了NERDTree没有其他文件时，它自动关闭，减少多次按:q!
 autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") &&b:NERDTreeType == "primary") | q | endif
"打开vim时自动打开NERDTree
"autocmd vimenter * NERDTree

"取消设置backup(~)文件
set nobackup
"开启鼠标
set mouse=a
"显示行号
set nu
"调节颜色
set background=dark
"代码（方法和类）折叠,按空格键
set foldmethod=indent
set foldlevel=99
nnoremap <space> za
"支持UTF-8编码
set encoding=utf-8
"代码高亮
let python_highlight_all=1
syntax on
"可以从Vim之外的程序中剪切、复制、粘贴文本
set clipboard=unnamed
"F5一键运行
   map <F5> :call CompileRunGcc()<CR>
    func! CompileRunGcc()
        exec "w"
        if &filetype == 'c'
            exec "!g++ % -o %<"
            exec "!time ./%<"
        elseif &filetype == 'cpp'
            exec "!g++ % -o %<"
            exec "!time ./%<"
        elseif &filetype == 'java'
            exec "!javac %"
            exec "!time java %<"
        elseif &filetype == 'sh'
            :!time bash %
        elseif &filetype == 'python'
            exec "!time python3.4 %"
        elseif &filetype == 'html'
            exec "!firefox % &"
        elseif &filetype == 'go'
    "        exec "!go build %<"
            exec "!time go run %"
        elseif &filetype == 'mkd'
            exec "!~/.vim/markdown.pl % > %.html &"
            exec "!firefox %.html &"
        endif
    endfunc

