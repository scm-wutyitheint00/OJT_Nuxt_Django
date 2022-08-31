<template>
  <div class="container">
    <h1>
      Post List
    </h1>
    <v-row>
      <v-col cols="3">
        <v-text-field v-model="search_term" label="Title" />
      </v-col>
      <v-col cols="2">
        <v-btn @click="searchPost()" name="submit-btn">Search</v-btn>
      </v-col>
      <v-col cols="2">
        <v-btn name="submit-btn" @click="addPost">Add</v-btn>
      </v-col>
      <v-col cols="2">
        <input type="file" ref="file" style="display: none" id="csv_file" name="csv_file" class="form-control"
          @change="loadCSV($event)" />
        <v-btn @click="$refs.file.click()">Upload</v-btn>
        <v-dialog v-model="dialog" width="500">
          <v-card>
            <v-card-title class="text-h5 grey lighten-2">
              Post Information
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text>
              <v-data-table :headers="csvHeaders" :items="csvDatas" :page.sync="page" @page-count="pageCount = $event"
                class="elevation-1">
              </v-data-table>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="warn" text @click="dialog = false">
                Cancel
              </v-btn>
              <v-btn color="primary" text @click="createCSV()">
                OK
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="confirmDialog" persistent max-width="290">
          <v-card>
            <v-card-title><span class="text-subtitle-1 text--primary">CSV creation successed!</span></v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" text @click="clickOK()">
                OK
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
      <v-col cols="2">
        <v-btn name="submit-btn" @click="downloadCSVData()">Download</v-btn>
      </v-col>
    </v-row>
    <v-data-table :headers="headers" :items="posts" :page.sync="page" :items-per-page="itemsPerPage" hide-default-footer
      @page-count="pageCount = $event" class="elevation-1">\
      <template v-slot:[`item.title`]="{ item }">
        <a href="#" @click="showPostDetail(item.id)">{{ item.title }}</a>
      </template>
      <template v-slot:[`item.created_at`]="{ item }">
        {{ (new Date(Date.now() - (new Date(item.created_at)).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)
        }}
      </template>
      <template v-slot:[`item.edit`]="{ item }">
        <nuxt-link :to="`/post/${item.id}/edit`"><a href="#">Edit</a></nuxt-link>
      </template>
      <template v-slot:[`item.delete`]="{ item }">
        <a @click="deleteId = item.id, deleteDialog = true">Delete</a>
      </template>
    </v-data-table>
    <div class="text-center pt-2">
      <v-pagination v-model="page" :length="pageCount"></v-pagination>
    </div>
    <v-dialog v-model="detailDialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="text-h5">Post Detail</span>
        </v-card-title>
        <v-card-text>
          <v-container fill-height fluid>
            <v-row justify="center">
              <v-col cols="3">
                <span class="text-subtitle-1 text--primary">Title</span>
              </v-col>
              <v-col cols="7">
                <span class="text-subtitle-1 text--primary">{{ this.postDetail.title }}</span>
              </v-col>
            </v-row>
            <v-row justify="center">
              <v-col cols="3">
                <span class="text-subtitle-1 text--primary">Description</span>
              </v-col>
              <v-col cols="7">
                <span class="text-subtitle-1 text--primary">{{ this.postDetail.description }}</span>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="detailDialog = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="deleteDialog" persistent max-width="290">
      <v-card>
        <v-card-title><span class="text-subtitle-1 text--primary">Are you sure to delete?</span></v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="deleteDialog = false">
            Cancel
          </v-btn>
          <v-btn color="green darken-1" text @click="deletePost()">
            Yes
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
window.axios = require('axios');
import exportFromJSON from "export-from-json";

export default {
  middleware: "auth",
  data() {
    return {
      page: 1,
      pageCount: 0,
      itemsPerPage: 7,
      dialog: false,
      confirmDialog: false,
      detailDialog: false,
      deleteDialog: false,
      deleteId: null,
      csvDatas: [],
      csvHeaders: [
        { text: 'Post Title', value: 'title' },
        { text: 'Post Description', value: 'description' }],
      headers: [
        {
          text: 'Post Title',
          align: 'start',
          sortable: false,
          value: 'title'
        },
        { text: 'Post Description', value: 'description' },
        { text: 'Posted User', value: 'updated_user_id' },
        { text: 'Posted Date', value: 'created_at' },
        { text: '', value: 'edit' },
        { text: '', value: 'delete' },
      ],
      posts: [],
      search_term: '',
      postDetail: {},
      datalogin: this.$store.getLoginData,
      isMember: ''
    }
  },
  created() {
    this.isMember = localStorage.getItem("isMember");
  },
  async asyncData({ $axios, params }) {
    let posts = await $axios.$get(`/posts/`)
    posts.edit = true;
    posts.delete = true;
    let isMember = localStorage.getItem("isMember");
    const userData = JSON.parse(localStorage.getItem('responseData'));
    if (isMember === 'true') {
      posts = posts.filter(post => {
        if (post.user === userData.id) {
          return post
        }
      })
    }
    return { posts };
  },
  methods: {
    addPost() {
      this.$router.push('/post/post-create');
    },
    async searchPost() {
      const userData = JSON.parse(localStorage.getItem('responseData'));
      await this.$axios.$get(`/posts?search=${this.search_term}`).then(data => {
        if (this.$store.state.isMember === 'true' || this.isMember === 'true') {
          this.posts = data.filter(post => {
            if (post.user === userData.id) {
              return post
            }
          })
        } else {
          this.posts = data
        }
      })
    },
    async deletePost() {
      try {
        const userData = JSON.parse(localStorage.getItem('responseData'));
        await this.$axios.$delete(`/posts/${this.deleteId}/`);
        await this.$axios.$get(`/posts`).then(data => {
          if (data.length > 0) {
            if (this.$store.state.isMember === 'true' || this.isMember === 'true') {
              this.posts = data.filter(post => {
                if (post.user === userData.id) {
                  return post
                }
              })
            } else {
              this.posts = data
            }
          } else {
            this.posts = []
          }
        })
        this.deleteDialog = false;
      } catch (e) {
        console.log(e);
      }
    },
    async createCSV() {
      this.dialog = false;
      this.csvDatas.forEach(data => {
        let postData = {
          title: '', description: '',
          created_at: new Date().toISOString(),
        }
        postData.title = data.title;
        postData.description = data.description;
        const userData = JSON.parse(localStorage.getItem('responseData'));
        postData.user = userData.id;
        postData.updated_user_id = userData.id;
        const config = {
          headers: { "content-type": "multipart/form-data" }
        };
        let formData = new FormData();
        for (let data in postData) {
          formData.append(data, postData[data]);
        }
        try {
          let response = this.$axios.$post(`/posts/`, formData, config);
          if (response) {
            this.confirmDialog = true;
            this.csvDatas = [];
          }
          this.$router.push("/post/");
        } catch (e) {
          console.log(e);
        }
      })
    },
    csvJSON(csv) {
      var vm = this
      const lines = csv.split('\n') // 1️
      lines.forEach(element => {
        element.replaceAll('"', '');
      });
      const header = lines[0].split(',') // 2️
      const output = lines.slice(1).map(line => {
        const fields = line.split(',') // 3️
        return Object.fromEntries(header.map((h, i) => [h, fields[i]])) // 4️
      })
      if (output.length > 0) {
        this.dialog = true;
        this.csvDatas = output;
      }
      return output // JavaScript object
    },
    loadCSV(e) {
      var vm = this
      if (window.FileReader) {
        let file = e.target.files[0];
        if (!file) { return }
        var reader = new FileReader();
        const xlsxMatch = file?.type.match(/^application\/vnd\.openxmlformats-officedocument\.spreadsheetml\.sheet$/gi);
        const csvTsvMatch = file?.type.match(/^text\/(csv|tab-separated-values)/gi);
        if (!file || (!xlsxMatch && !csvTsvMatch && !file.name.match(/\.(xlsx|csv)$/gi))) {
          alert("Canno't read file !");
        } else {
          reader.readAsText(e.target.files[0]);
          reader.onload = function (event) {
            var csv = event.target.result;
            vm.parse_csv = vm.csvJSON(csv.replaceAll('"', ''))
          };
        }
      } else {
        alert('FileReader are not supported in this browser.');
      }
    },
    async downloadCSVData() {
      let posts = await this.$axios.$get(`/posts/`);
      const data = this.posts;
      const downloadData = new Date().toLocaleDateString(['ban', 'id']);
      const fileName = `post-list_${downloadData}.csv`;
      const exportType = exportFromJSON.types.csv;
      if (data) exportFromJSON({ data, fileName, exportType });
    },
    async showPostDetail(postId) {
      this.postDetail = await this.$axios.$get(`/posts/${postId}`);
      this.detailDialog = true;
    },
    async clickOK() {
      const userData = JSON.parse(localStorage.getItem('responseData'));
      this.confirmDialog = false;
      await this.$axios.$get(`/posts`).then(data => {
        if (data.length > 0) {
          if (this.$store.state.isMember === 'true' || this.isMember === 'true') {
            this.posts = data.filter(post => {
              if (post.user === userData.id) {
                return post
              }
            })
          } else {
            this.posts = data
          }
        } else {
          this.posts = []
        }
      })
    }
  }
}
</script>

<style scoped>
h1 {
  margin-bottom: 50px;
}

a {
  color: blue;
  text-decoration: underline;
}
</style>