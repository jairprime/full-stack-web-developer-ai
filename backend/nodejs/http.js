const http = require("http");

http
  .createServer((request, response) => {
    console.log(request.url);

    if (request.url === "/") {
      response.write("welcome to the server");
      return response.end();
    }

    if (request.url === "/about") {
      response.write("acerca de");
      return response.end();
    }

    response.write("Not found");
    response.end();
  })
  .listen(3000);

console.log("Server listening on port 3000");
