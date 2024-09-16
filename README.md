# final-project
## Ques in layout (alert) - finance
 I don't know why my finance web doesn't have any alert even in my layout.html has one. What is the problem with the function get_flashed_message()? It from jinja, is it?

if you want to read like adocument: delete these '''
'''
    {% if get_flashed_messages() %}
        <header>
            <div class="alert alert-primary mb-0 text-center" role="alert">
                {{ get_flashed_messages() | join(" ") }}
            </div>
        </header>
    {% endif %}

## Ques in check html (i love validator) - finance
I'm not really understand this :
        <footer class="mb-5">
            <form action="https://validator.w3.org/check" class="text-center" enctype="multipart/form-data" method="post" target="_blank">
                <input name="doctype" type="hidden" value="HTML5">
                <input name="fragment" type="hidden">
                <input alt="Validate" src="/static/I_heart_validator.png" type="image"> <!-- https://validator.w3.org/ -->
            </form>
            <script>
                document.addEventListener('DOMContentLoaded', function() {
                    // Adapted from https://stackoverflow.com/a/10162353
                    const html = '<!DOCTYPE ' +
                    document.doctype.name +
                    (document.doctype.publicId ? ' PUBLIC "' + document.doctype.publicId + '"' : '') +
                    (!document.doctype.publicId && document.doctype.systemId ? ' SYSTEM' : '') +
                    (document.doctype.systemId ? ' "' + document.doctype.systemId + '"' : '') +
                    '>\n' + document.documentElement.outerHTML;
                    document.querySelector('form[action="https://validator.w3.org/check"] > input[name="fragment"]').value = html;
                });
            </script>
        </footer>

## nav bar: I want to make it more beautiful
Solution to have full page image: no nav

## container aranging:
https://css-tricks.com/snippets/css/a-guide-to-flexbox/

## footer to the bottom but not the left

## Register: how to redirect to login and auto log user in

## How to create transparent box in css:
[Link to guide](https://developer.mozilla.org/en-US/docs/Learn/CSS/Howto/Make_box_transparent)

## Option in quest: use a loop? : no one can fix my code

## I want seperate box of quest but it just come all in one huge box :). So I decided to turn into select but yeh, I still want boxes
<div>
    <section class="quiz-section">
        {% for question in questions %}
        <div class="quiz-box">
            <h3 class="question">{{question}}</h3>
            <div class="option-list">
                {% for option in options %}
                <div class="option">
                    <span class="handlee-regular">{{option}}</span>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endfor %}
    </section>
</div>

## I tryed to make radio choices in mbti test page but I forgot to change the options' name:
### First I do like this so the choices in question 1 will disapper when I make another choice in question 2 because the program thought that 2 question is same: <notice that the name of every options is all option>
{% for i in range(32) %}
    {% if i % 2 == 0 %}
    <form class="quiz-box2">
        <h4 class="question">{{ questions[i] }}</h4>
        {% for option in options %}
        <input name="option" type="radio" value="{{i}}" style="font-size: medium;">{{option}}
        {% endfor %}
    </form>
    {% else %}
    <form class="quiz-box1">
        <h4 class="question">{{ questions[i] }}</h4>
        {% for option in options %}
        <input name="option" type="radio" value="{{i}}" style="font-size: medium;">{{option}}
        {% endfor %}
    </form>
    {% endif %}
{% endfor %}
### but now I change name in input into i so the name of options in one question is the same but in two separate question it is different
{% for i in range(32) %}
    {% if i % 2 == 0 %}
    <form class="quiz-box2">
        <h4 class="question">{{ questions[i] }}</h4>
        {% for option in options %}
        <input name="{{i}}" type="radio" value="{{i}}" style="font-size: medium;">{{option}}
        {% endfor %}
    </form>
    {% else %}
    <form class="quiz-box1">
        <h4 class="question">{{ questions[i] }}</h4>
        {% for option in options %}
        <input name="{{i}}" type="radio" value="{{i}}" style="font-size: medium;">{{option}}
        {% endfor %}
    </form>
    {% endif %}
{% endfor %}


### problem with request.form.get:
Request return nontype 
I checked in finance and turn out it just return nontype when it get nothing
I checked back in test.html : forms has no post method -> chenge method into post for every form
->> change action ="/test"
because I edit and use request for route "/test" so I must add action="/test" in the form in html else /test cannot get anything in that form