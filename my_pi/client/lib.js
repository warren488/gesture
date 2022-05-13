
let vidIndex = 0;

let fullPlaylist = [
  {
    "title": "Data Structures and Algorithms in JavaScript - Full Course for Beginners",
    "image": "https://i.ytimg.com/vi/t2CEgPsws3U/maxresdefault.jpg",
    "description": "Learn common data structures and algorithms in this tutorial course. You will learn the theory behind them, as well as how to program them in JavaScript.⭐️ C...",
    "url": "https://www.youtube.com/watch?v=t2CEgPsws3U"
  },
  {
    "title": "11 TTL option for streaming in Chart JS | Chartjs Plugin Streaming Series",
    "image": "https://i.ytimg.com/vi/a5EzDfR-2u8/maxresdefault.jpg",
    "description": "11 TTL option for streaming in Chart JS | Chartjs Plugin Streaming SeriesIn this video we will explore how to use the ttl option for streaming in Chart JS. W...",
    "url": "https://www.youtube.com/watch?v=a5EzDfR-2u8"
  },
  {
    "title": "Psychic Signatures (Java Vulnerability) - Computerphile",
    "image": "https://i.ytimg.com/vi/502iGDxuiRk/hqdefault.jpg",
    "description": "The psychic paper in the TV show \"Doctor Who\" displays whatever the Doctor needs it to show at any given time. The Java vulnerability Neil Madden exposed is ...",
    "url": "https://www.youtube.com/watch?v=502iGDxuiRk"
  },
  {
    "title": "Socket.IO with Python and JavaScript",
    "image": "https://i.ytimg.com/vi/tHQvTOcx_Ys/maxresdefault.jpg",
    "description": "This tutorial has 10 parts. Below you can find the direct links to each of the chapters:00:00:00 Part 1: Socket.IO Server (Python)00:09:27 Part 2: Socket.IO ...",
    "url": "https://www.youtube.com/watch?v=tHQvTOcx_Ys"
  }
]

let htmlstring = ''
fullPlaylist.forEach(data => {
  htmlstring += `
            <div class="card mb-3" style="max-width: 540px;width:380px">
                <img src="${data.image}" class="img-fluid rounded-start" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${data.title}</h5>
                    <p class="card-text d-none">${data.description}</p>
                    <p class="card-text"><small class="text-muted">${data.url}</small></p>
                </div>
            </div>`
})
document.querySelector('.list').innerHTML = htmlstring;
let player;
window.onYouTubeIframeAPIReady = function onYouTubeIframeAPIReady() {
  window.player = new YT.Player('player', {
    height: '390',
    width: '640',
    videoId: getVidId(fullPlaylist[vidIndex].url),//'M7lc1UVf-VE',
    playerVars: {
      'playsinline': 1
    },
    events: {
    }
  });
}


export function stopVideo() {
  player.stopVideo();
}
export function incrementVidIndex(increment = 1) {
  vidIndex = (vidIndex + increment) % fullPlaylist.length
  return vidIndex
}
export function decrementVidIndex() {
  if (vidIndex === 0) {
    vidIndex = fullPlaylist.length - 1
    return vidIndex
  } else {
    vidIndex--
    return vidIndex
  }
}
export function getVidId(link) {
  let vidId;
  try {
    let url = new URL(link);
    if (url.hostname === "www.youtube.com") {
      vidId = url.searchParams.get("v");
    } else if (url.hostname === "youtu.be") {
      vidId = url.pathname.substr(1);
    } else {
      return vidId;
    }
    return vidId;
  } catch (e) {
    console.log(e);
  }
}
export function playNext() {
  let url = fullPlaylist[incrementVidIndex()].url;
  console.log(url)
  // window.player.destroy()
  // window.player = new YT.Player('player', {
  //   height: '390',
  //   width: '640',
  //   videoId: getVidId(url),//'M7lc1UVf-VE',
  //   playerVars: {
  //     'playsinline': 1
  //   },
  //   events: {
  //     // 'onReady': onPlayerReady,
  //     // 'onStateChange': onPlayerStateChange
  //   }

  // });
  window.player.cueVideoById(getVidId(url))
}
export function playPrevious() {
  let url = fullPlaylist[incrementVidIndex()].url;
  window.player.destroy()
  window.player = new YT.Player('player', {
    height: '390',
    width: '640',
    videoId: getVidId(url),//'M7lc1UVf-VE',
    playerVars: {
      'playsinline': 1
    },
    events: {
      // 'onReady': onPlayerReady,
      // 'onStateChange': onPlayerStateChange
    }
  });
}

export function volumeUp(){
  window.player.setVolume(window.player.getVolume() + 5)
}
export function volumeDown(){
  window.player.setVolume(window.player.getVolume() - 5)
}