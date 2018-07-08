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
    },
    startInterval: function() {
      const self = this;
      setInterval(function() {
        axios
          .get("http://moiseev.tk/temppi.php")
          .then(response => {
            self.pi_term = response.data;
          })
          .catch(error => {
            console.log(error);
            self.errored = true;
          })
          .finally(() => (self.loading = false));
      }, 2500);
    }
  },
  mounted() {
    this.startInterval();
  }
});
