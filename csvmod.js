const fs = require('fs')
const { getChangeInVelocity } = require('./test')

fs.readFile('./xswing.csv', 'utf8', (err, data) => {
    if (err) {
        console.error(err)
        return
    }
    let file = data;
    let lines = file.split('\n');
    let headings = lines.shift();
    for (let i = 0; i < lines.length; i++) {
        lines[i] = lines[i].split(',')
        // console.log(lines[i]);
        for (let j = 0; j < lines[i].length; j++) {
            lines[i][j] = Number(lines[i][j]);
        }
        lines[i].push(Number(lines[i - 1]?.[lines[i - 1].length - 1] || 0) + getChangeInVelocity((lines[i - 1]?.[1] - 0.1 || 0), lines[i][1] - 0.1, (lines[i - 1]?.[0] || lines[i][0]), lines[i][0]))

        // lines[i] = lines[i].join(',')
    }
    console.log(getChangeInVelocity(0.08556473255, 0.02080127597, 31.14585234, 31.15093197))
    console.log(lines[lines.length - 2]);
    console.log(lines[lines.length - 1]);
    headings += ',vx'
    lines.unshift(headings)
    fs.writeFile('./xs.csv', lines.join('\n'), err => {
        if (err) {
            console.error(err)
            return
        }
        //file written successfully
    })
})