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
