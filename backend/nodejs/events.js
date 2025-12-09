const EventEmitter = require('events')

const customEmitter = new EventEmitter()

customEmitter.on('x', (data, secondData) => {
    console.log('received');
    console.log(secondData);
})

customEmitter.emit('x', 'fazt', [1,2,3])



