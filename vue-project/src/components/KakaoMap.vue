<template>
  <div class="r">
  </div>
  <div id="map"></div>
  <!-- 하얀색 박스를 표시할 요소 -->
  <div v-if="showInfoWindow" class="info-window" style="top: 30%; left: 50%; transform: translate(-50%, -50%);">
    <h3>하우스베이커리</h3>
    <p>위치 : 경기 양평군 서종면 북한강로 684 하우스베이커리</p>
    <span>운영 시간 :10:30~20:00
 </span>
    <span>전화번호 : 0507-1447-8337
</span>
<span>기타 : 화장실있음, 주차장 있음, 좌석 있음
 </span>
 
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "KakaoMap",
  data() {
    return {
      map: null,
      showInfoWindow: false // 마커에 마우스를 올렸을 때 정보창을 표시할지 여부를 나타내는 데이터
    };
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.loadMap();
    } else {
      this.loadScript();
    }
  },
  methods: {
    loadScript() {
      const script = document.createElement("script");
      script.src =
        "//dapi.kakao.com/v2/maps/sdk.js?appkey=7c23a6348a4f94dffebfdeb814578f7c&autoload=false";
      script.onload = () => window.kakao.maps.load(this.loadMap);
      document.head.appendChild(script);
    },
    loadMap() {
      const container = document.getElementById("map");
      const options = {
        center: new window.kakao.maps.LatLng(37.5988115, 127.353289),
        level: 12,
      };

      this.map = new window.kakao.maps.Map(container, options);

      // 마커 생성 및 추가
      const markerPosition = new window.kakao.maps.LatLng(37.5988115, 127.353289);
      const marker = new window.kakao.maps.Marker({
        position: markerPosition,
        map: this.map // 이 마커를 현재 생성한 지도에 추가합니다.
      });

      // 마커에 마우스 이벤트 추가
      window.kakao.maps.event.addListener(marker, 'mouseover', () => {
        this.showInfoWindow = true; // 마우스를 올렸을 때 정보창 표시
      });
      window.kakao.maps.event.addListener(marker, 'mouseout', () => {
        this.showInfoWindow = false; // 마우스를 내렸을 때 정보창 숨김
      });
    },
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: white;
}
.r {
  float: right;
  margin-top: 100px;
}
.r button {
  text-decoration: none;
  text-align: center;
  color: black;
}
#map {
  width: 100%;
  height: 1000px;
}
.info-window {
  position: fixed; /* 고정 위치로 변경 */
  background-color: white;
  padding: 10px;
  border: 1px solid #ccc;
  z-index: 1;
  width:40%;
  height:25%;
}
span{display: block;
     padding-bottom:10px;}
    
h3{padding-bottom:10px;
  padding-top:10px;}
</style>
