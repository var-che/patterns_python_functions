## Take one, attaching specific functions outside the markup_text,
## as a instructions (conditions) what of functions you want to be executed
## at a time.


def markup_text(text, *responsibilities):

    temp_text = text

    for tag in responsibilities:
        if tag == 'b': temp_text = '%s%s%s' % ('<b>', temp_text, '</b>')#; print ("Bold wrapping executed on " + text)
        if tag == 'i': temp_text = '%s%s%s' % ('<i>', temp_text, '</i>')#; print ("Italic wrapping executed on " + text)

    print (temp_text)

## simple demonstraion using efficient wrappings
## around some default object (string in this case)

markup_text("Text without markup.")
markup_text("Wrap me around stuff.", *['b', 'i', 'b'])
markup_text("Just italic, thank you.", *['i'])

## OUTPUT
# Text without markup.
# <b><i><b>Wrap me around stuff.</b></i></b>
# <i>Just italic, thank you.</i>

## Take two
def markup_textt(text):
    ## prints before anything
    ##
    ## print("this is markup_textt's line that will be executed first")
    def italic():
        inner_text = text()
        inner_text =  "%s%s%s" % ('<i>', inner_text, '</i>')
        return inner_text
    return italic

@markup_textt ## is the same as text = markup_textt(text)
def text():
    return ("this is just a string")

print(text())

## OUTPUT
# <i>this is just a string</i>

################################################################################
## TODO Experiment with wrappers, but above all, keep in mind the data structure
