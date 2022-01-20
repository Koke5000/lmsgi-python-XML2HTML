file = open('output/index.html', 'w')
document = ''
document += '<html>'
document += '<body>'
document += '<p>Esto es una prueba de escritura desde python</p>'
document += '</body>'
document += '</html>'
file.write(document)
