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