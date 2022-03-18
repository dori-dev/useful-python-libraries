"""textwrap library
"""

import textwrap

TEXT = '''
    Lorem ipsum dolor sit amet consectetur adipisicing. Maxime mollitia,
    molestiae quas vel sint commodi repudiandae consequuntur voluptatum
    numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga
    optio, eaque rerum! Provident similique accusantium nemo autem.
    Veritatis obcaecati tenetur iure eius earum ut molestias architecto
    voluptate aliquam nihil, eveniet aliquid culpa officia aut! Impedit
    tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit,
    quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos
    sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
    recusandae alias error harum maxime adipisci amet laborum. Perspiciatis
    minima nesciunt dolorem! Officiis iure rerum voluptates a cumque velit
'''

print("\n\ntext")
print(TEXT)

# wrap, slice the text
print("\n\nwrap()")
print(textwrap.wrap(TEXT, width=80))

# fill, style the text for good show
print("\n\nfill()")
print(textwrap.fill(TEXT, width=50))

# shorten, convert text to short text
# default of placeholder is [...]
print("\n\nshorten()")
print(textwrap.shorten(TEXT, width=150, placeholder=' ... '))

# dedent, deleted the indent of text
print("\n\ndedent()")
print(textwrap.dedent(TEXT))

# indent, insert the string before text indent
print("\n\nindent()")
print(textwrap.indent(TEXT, prefix='=> '))

# TextWrapper, get any param and use there in other functions
print("\n\nTextWrapper()")
string = textwrap.TextWrapper(expand_tabs=True, tabsize=1)
print(string.fill(TEXT))
