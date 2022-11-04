<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div class="book-box">
      <h2>예약 페이지</h2>
      <div class="time-board">
        <h3>시간 선택</h3>
        <button 
          class="time-btn"
          v-for="time in times" :key="time"
          :class="{selected: selTimeList.includes(time)}"
          @click="btnClick"
        >
          {{ time }}
        </button>
      </div>
      <div class="sel-time-box">
        <span>선택시간: </span>
        <span 
          id="sel-time" 
          v-for="selTime in selTimeList" 
          :key="selTime"
        >
          {{selTime}}
        </span>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data: function() {
    return{
      times: [
        "00:00","00:30","01:00","01:30","02:00","02:30","03:00","03:30",
        "04:00","04:30","05:00","05:30","06:00","06:30","07:00","07:30",
        "08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30",
        "12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30",
        "16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30",
        "20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selTimeList: []
    }
  },
  methods: {
    btnClick(e){
      const time = e.target.innerText
      const index = this.selTimeList.indexOf(time)
      if (index >= 0) {
        // console.log(index)
        this.selTimeList.splice(index, 1)
      }
      else if (this.selTimeList.length < 5) {
        this.selTimeList.push(time)
        this.selTimeList.sort()
      } else {
        alert('5개 이하만 선택 가능합니다!')
      }
    }
  }
}
</script>

<style>
  /* 
  #0f4c85 버튼 클릭 시 버튼 글씨 색
  #658dc63d 버튼 클릭 시 버튼 배경색
  #84898c 버튼 글씨 색
  #424242 전체 글씨 색
  */
  @font-face {
    font-family: 'Noto Sans KR';
    font-style: normal;
    font-weight: 700;
    src: url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Bold.woff2) format('woff2'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Bold.woff) format('woff'),url(//fonts.gstatic.com/ea/notosanskr/v2/NotoSansKR-Bold.otf) format('opentype');}

  #app {
    font-family: Noto Sans KR, Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #424242;
    margin-top: 60px;
  }

  .book-box {
    box-shadow: 1px 2px 2px 2px #ddd4d4;
    width: 480px;
    padding: 5px;
    margin: auto;
  }

  .time-btn{
    width: 60px;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    background-color: white;
    border: none;
    font-size: 15px;
    color: #84898c;
  }
  .time-btn:hover{
    cursor: pointer;
  }
  .time-board{
    margin-bottom: 30px;
  }
  .sel-time-box{
    width: 400px;
    margin: auto;
    padding: 10px;
    border-top: 1px solid black;
  }
  #sel-time{
    margin-right: 5px;
  }
  .selected{
    color: #0f4c85;
    background-color: #658dc63d;
  }
</style>
