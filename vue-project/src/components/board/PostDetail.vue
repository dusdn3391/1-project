<template>
  <div class="board-detail">
    <div class="common-buttons">
      <button type="button" class="w3-round" v-on:click="fnDelete">삭제</button>&nbsp;
      <button type="button" class="w3-button w3-round w3-gray" v-on:click="fnList">목록</button>
    </div>
    <div class="board-title">
      <h2>공유 게시판</h2>
    </div>
    <div class="board-content">
      <h5>구해요</h5>
      <div class="board-name">
        <strong class="w3-large">최연우</strong>
        <br>
        <span>2023-08-27</span>
      </div>
    </div>
    <div class="board-contents">
      <span>경기도에 있는 무화과 케이크 구해요 혹시 구매하셔서 서울로 올라오시는 분 부탁드리겠습니다
        만나는 장소는 채택되시면 연락드리겠습니다.
      </span>
    </div>
    <div class="common-buttons">
      
      <button type="button" class="w3-button w3-round w3-red" v-on:click="fnDelete">삭제</button>&nbsp;
      <button type="button" class="w3-button w3-round w3-gray" v-on:click="fnList">목록</button>
    </div>
  </div>
</template>

<script>
export default {
  data() { //변수생성
    return {
      requestBody: this.$route.query,
      idx: this.$route.query.idx,

      title: '',
      author: '',
      contents: '',
      created_at: ''
    }
  },
  mounted() {
    this.fnGetView()
  },
  methods: {
    fnGetView() {
      this.$axios.get(this.$serverUrl + '/board/' + this.idx, {
        params: this.requestBody
      }).then((res) => {
        this.title = res.data.title
        this.author = res.data.author
        this.contents = res.data.contents
        this.created_at = res.data.created_at
      }).catch((err) => {
        if (err.message.indexOf('Network Error') > -1) {
          alert('네트워크가 원활하지 않습니다.\n잠시 후 다시 시도해주세요.')
        }
      })
    },
    fnList() {
      delete this.requestBody.idx
      this.$router.push({
        path: './postlist',
        query: this.requestBody
      })
    },
    fnDelete() {
      if (!confirm("삭제하시겠습니까?")) return

      this.$axios.delete(this.$serverUrl + '/board' + this.idx, {})
          .then(() => {
            alert('삭제되었습니다.')
            this.fnList();
          }).catch((err) => {
        console.log(err);
      })
    }
  }
}
</script>
<style scoped>
.board-title{margin-top:80px;
             margin-bottom:20px;
             border-bottom:2px solid rgb(193, 139, 73);
            }
.board-detail{width:90%;
              margin:0 auto;}

h5{font-weight:700;}

.board-name span{font-weight:500;
                color:rgb(164, 164, 164)}

.board-contents{padding:10px;
                padding-top:30px;
                padding-bottom:50px;;}

.common-button{width:90%;
              margin:0 auto;}

.w3-button{background-color:#fff;}
</style>