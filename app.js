new Vue({
  el: "#app",
  data: {
    show_cam: false,
    message: "Привет, Vue.js!",
    url_cam: "",
    pi_term: "",

    info: null,
    loading: true,
    errored: false
  },
  methods: {
    show_citch: function(e) {
      if (this.show_cam) {
        this.url_cam = "";
      } else {
        this.url_cam = "cam.php";
        //this.url_cam = "http://5.79.154.148:8881";
      }
      this.show_cam = !this.show_cam;
    }
  },
  mounted() {
    axios
      .get("temppi.php")
      .then(response => {
        this.pi_term = response.data.response;
      })
      .catch(error => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  }
});
