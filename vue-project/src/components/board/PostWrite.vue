<template>
  <div class="board-detail">
    <div class="write_title">
      <h2>공유게시판</h2>
    </div>
    <div class="board-contents">
      <input type="text" v-model="title" class="w3-input w3-border" placeholder="제목을 입력해주세요.">
      <input type="text" v-model="author" class="w3-input w3-border" placeholder="작성자를 입력해주세요." v-if="idx === undefined">
    </div>
    <div class="board-contents">
      <textarea id="" cols="30" rows="10" v-model="contents" class="w3-input w3-border" style="resize: none;">
      </textarea>
    </div>
    <div class="common-buttons">
      <button type="button" class="w3-button w3-round w3-blue-gray" v-on:click="fnSave"><router-link to="/board/postdetail">저장</router-link></button>&nbsp;
      <button type="button" class="w3-button w3-round w3-gray" v-on:click="fnList"><router-link to="/board/postlist">목록</router-link></button>
    </div>
  </div>
</template>

<script>

</script>
<style scoped>
a{text-decoration:none;
 color:white;
 }

.board-detail{padding:50px;
              padding-top:150px;}
.write_title{padding-bottom:20px;}
.common-buttons{margin-top:30px;}
</style>