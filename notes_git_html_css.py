'''
Git clone - 

Git commit - take a snapshot of the repository in the current moment and save it. Fancy way of saying Save.

git status - what's currently going on in your repository . 

git log - shows you a histroy of all the commits that were made. It'll show each commit with a hash.

git reset - 
    We can use git reset --hard <commit> 
    or git reset --hard origin/master
Ex. git reset --hard <commit hash> 
Will change the head to <commit hash> <commit message> .
Any changes done locally will never effect the repository on github UNLESS we do a push. 


Simpler command
git commit -am 
This will do both add and commit in one command. 


git reference log:
git reflog 

HEAD means where we are in the repository right now. 
'''


'''
HTML website 
Think of it as a tree structure.
Nodes - where nodes are just points within this tree that's connected to other nodes.

Document object model:
HTML tag leads to:
head> title > Hello!
body > h1 > hello world!

div - division a section of my code. Incase I want to do something specific to it, like style it. A section of the web page.
Span - section of the web page that is in the middle of some text. 
Both are labeling the section of the web page. 

Assign a section a div and specify an ID to it. 
<div id = 'top'> 

class - an attribute to give name to a specific type of element element as well. 
Can group many things to a class. 

div's id attribute can only be assigned one element, unique.

Class and IDs are both used to identify elements. 

If there's conflicts, css will pick the more specific option. 
If something's more deeper within the tree, css will pick that option. 
'''



'''
CSS:
Linking a css file :
<link rel="stylesheet" href="variables.css">

hex color - 0 means very little of a certain color and 255 means a lot of that color
Goes by RBG - red , green, blue .
in css: style= "color:#0c8e05;text-align:center;"
 

The # sign in CSS means ID. 


The "." in css means class. 

css selector's '>' takes the immediate child. 

To add something to the beginning or end of a link, use colon colon.
Ex. a:: after 
or 
a:: before 

Selection:
p::selection{
    color:red;
    back-ground:yellow;
}
When text is selected, perform this action.


CSS Selectors
a,b  - multiple element selector
a b descendat selector
a > b child selector
a + b adjacent sibling selector
[a=b] attribute selector
a:b pseudoclass selector
a::b pseudoelement selector

To make your web page fit on mobile devices, you should add the meta tag:
<meta name ='viewport' content = 'width=device-wdith, initial-scale=1.0'> 
@media (max-wdith: 499px) {}

@media (min-width: 500px){}

Flex
.container {
    display:flex;
    flex-wrap:wrap;
}


Nesting css:
The following means any ul or p tags inside a div will be effected by the following style:
div {
    font-size:19px;
    
    p{
        color:blue;
    }
    ul{
        color:green;
    }
}

'''


'''
Bootstrap: 
There's 12 columns that can be taken up. 

<div class="col-lg-3 col-sm-6"

bootstrap classes:
- container

alerts:
<div class="alert alert-success" - blue message

<div class="alert alert-primary" - green message

<div class="alert alert-danger" - red message
'''



'''
Sass  - An extension to CSS. programatically generate style sheets. Makes it easier to generate style sheet.
scss is the extension to a Sass file.
You need to install sass. 

Define a variable:
always start with a dollar sign $.
- $color: red;

ul{
    font-size:14px;
    color: $color;
}

ol {
    font-size: 10px;
    color: $color;
}

You will need to compile the scss file to a css file so that it can be read:
- sass variables.scss variables.css
Instead of the doing the command above everytime you make a change, you can have sass watch the file for changes. 
It will then recompile everytime a change is made.
sass -- watch variables.scss:variables.css


% is specific to sass. 
% is creating a template for other things to inherit from.
Ex.:
%message{
    font-family: sans-serif;
    font-size:18px;
    font-weight:bold;
    border:1px solid black;
    padding: 20px;
    margin:20px;
} 

Use @extend to tell the class to all the styling in the message template, additional make the background-color the specified color.
.success{
    @extend %message;
    background-color:green;
}

.warning{
    @extend %message;
    background-color: orange;
}

.error{
    @extend %message;
    background-color: red;
}
'''