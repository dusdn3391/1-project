<template>
  <div class="board-list">
    <div class="list_title">
      <h2>공유게시판</h2>
    </div>
    <div class="common-buttons">
      <router-link to="/board/PostWrite"><button type="button" class="w3-button w3-round w3-blue-gray">등록</button></router-link>
    </div>
    <table class="w3-table-all">
      <thead>
      <tr>
        <th>No</th>
        <th>제목</th>
        <th>작성자</th>
        <th>등록일시</th>
      </tr>
      </thead>
      <tbody>
  <tr>  
    <td>1</td>
    <td>
      <router-link to="/board/postdetail">교환</router-link>
    </td>
    <td>최연우</td>
    <td>2024.04.30</td>
  </tr>
  
  <tr>
    <td>2</td>
    <td>
      <router-link to="/board/postdetail">부산이동</router-link>
    </td>
    <td>방형욱</td>
    <td>2024.04.30</td>
  </tr>
</tbody>
    </table>
    <div class="pagination w3-bar w3-padding-16 w3-small" v-if="paging.total_list_cnt > 0">
      <span class="pg">
      <a href="javascript:;" @click="fnPage(1)" class="first w3-button w3-bar-item w3-border">&lt;&lt;</a>
      <a href="javascript:;" v-if="paging.start_page > 10" @click="fnPage(`${paging.start_page-1}`)"
         class="prev w3-button w3-bar-item w3-border">&lt;</a>
      <template v-for=" (n,index) in paginavigation()">
          <template v-if="paging.page==n">
              <strong class="w3-button w3-bar-item w3-border w3-green" :key="index">{{ n }}</strong>
          </template>
          <template v-else>
              <a class="w3-button w3-bar-item w3-border" href="javascript:;" @click="fnPage(`${n}`)" :key="index">{{ n }}</a>
          </template>
      </template>
      <a href="javascript:;" v-if="paging.total_page_cnt > paging.end_page"
         @click="fnPage(`${paging.end_page+1}`)" class="next w3-button w3-bar-item w3-border">&gt;</a>
      <a href="javascript:;" @click="fnPage(`${paging.total_page_cnt}`)" class="last w3-button w3-bar-item w3-border">&gt;&gt;</a>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  data() { //변수생성
    return {
      requestBody: {}, //리스트 페이지 데이터전송
      list: {}, //리스트 데이터
      no: '', //게시판 숫자처리
      paging: {
        block: 0,
        end_page: 0,
        next_block: 0,
        page: 0,
        page_size: 0,
        prev_block: 0,
        start_index: 0,
        start_page: 0,
        total_block_cnt: 0,
        total_list_cnt: 0,
        total_page_cnt: 0,
      }, //페이징 데이터
      page: this.$route.query.page ? this.$route.query.page : 1,
      size: this.$route.query.size ? this.$route.query.size : 10,
      keyword: this.$route.query.keyword,
      paginavigation: function () { //페이징 처리 for문 커스텀
        let pageNumber = [] //;
        let start_page = this.paging.start_page;
        let end_page = this.paging.end_page;
        for (let i = start_page; i <= end_page; i++) pageNumber.push(i);
        return pageNumber;
      }
    }
  },
  mounted() {
    this.fnGetList()
  },
  methods: {
    fnGetList() {
      // 서버로부터 게시물 데이터를 가져오는 API 호출
      this.$axios.get(this.$serverUrl + "/board/get_all_post")
        .then((response) => {
          // 가져온 데이터를 this.list에 할당
          this.list = response.data.posts;
        })
        .catch((error) => {
          console.error('Error loading posts:', error);
          // 에러 처리
        });
        }
      }
    };
</script>
<style scoped>
.board-list{padding:50px;
            padding-top:100px;}
a{text-decoration:none;
  color:#000;
  display: block;}
button{float:right;}

</style>