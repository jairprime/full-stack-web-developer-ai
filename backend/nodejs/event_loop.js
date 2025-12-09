const http = require('http')

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.write('Welcome to the server')
        return res.end()
    }

    if (req.url === '/about') {
        res.write('about page')
    }

    res.end('not found')

})

server.listen(3000)
console.log('server on port 3000');