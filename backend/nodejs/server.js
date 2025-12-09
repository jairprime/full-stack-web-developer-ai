const http = require('http')

const server = http.createServer((req, res) => {
    if(req.url === '/') {
        res.write('Welcome to node.js!')
        return res.end()
    }
    if (req.url === '/about') {
        res.write('Page about')
        return res.end()
    }

    return res.end('not found')

})

server.listen(3000)
console.log('Server on port 3000')