// https://www.last.fm/api => 여기서 API 신청
const searchInput = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')  

let page = 1 
let limit = 100
searchInput.addEventListener('click', fetchAlbums)

const sentinel = document.createElement('div')
sentinel.id = 'sentinel'
createObserver(sentinel)

async function fetchAlbums(page=1, limit=100) {
  // (advanced) 로더
  const loadingList = document.querySelector('.search-result--loadingList')
  loadingList.style.display = 'block'

  const keyword = document.querySelector('.search-box__input').value
  if (!keyword.trim()) return
  
  // API 키 삽입
  const API_KEY = 'API 키를 삽입하세요'
  const BASE_URL = 'http://ws.audioscrobbler.com/2.0/'
  const searchUrl = `?method=album.search&format=json`
  const params = {
    api_key: API_KEY,
    album: keyword,
    page: 1,
    limit: 100,
  }
  
  const requestUrl = BASE_URL + searchUrl
  const res = await axios.get(requestUrl, { params })
  const albums = res.data.results.albummatches.album
  
  // (advanced) 로더
  loadingList.style.display = 'none'
  appendAlbumCards(albums)
}

function appendAlbumCards(albums) {
  const cardList = document.createDocumentFragment() // Optimized Version
  albums.forEach(album => {  
    
    // left side's image tag
    const cardImg = document.createElement('img')
    cardImg.src = album.image[1]['#text']
    
    // right side content
    const cardArtistName = document.createElement('h2')
    const cardAlbumName = document.createElement('p')
    cardArtistName.innerText = album.artist
    cardAlbumName.innerText = album.name
    
    // right side box
    const cardText = document.createElement('div')
    cardText.classList.add('search-result__text')
    cardText.append(cardArtistName, cardAlbumName)
    
    // card (left + right)
    const card = document.createElement('div')
    card.classList.add('search-result__card')
    card.append(cardImg, cardText)
    card.addEventListener('click', () => {
      window.location.href = album.url
    })

    cardList.appendChild(card)
  })
  
  searchResult.append(cardList)
  searchResult.append(sentinel) // (advanced) Infinite Scrolling
}


/* 
  ===== 
  (advanced) Infinite Scrolling
  =====
*/
function createObserver(target) {
  const getMoreAlbums = (entries) => {
    entries.forEach(entrie => {
      if (entrie.isIntersecting) {
        page += 1
        fetchAlbums(page)
      }
    })
  }
  
  const observer = new IntersectionObserver(getMoreAlbums);
  observer.observe(target); 
}
