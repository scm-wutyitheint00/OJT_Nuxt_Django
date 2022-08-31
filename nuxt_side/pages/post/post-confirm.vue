<template>
  <div class="container">
    <h1 class="title">
      Confirm Post
    </h1>
    <v-form>
      <v-row>
        <v-col cols="4">
          <v-subtitle>Title</v-subtitle>
        </v-col>
        <v-col class="text-left" cols="5">
          <p class="text-subtitle" value="this.confirmData.title">
            {{ $store.state.posts.title }}
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="4">
          <v-subtitle>Description</v-subtitle>
        </v-col>
        <v-col  class="text-left" cols="5">
          <p class="text-subtitle" value="this.confirmData.description">
            {{ $store.state.posts.description }}
          </p>
        </v-col>
      </v-row>
      <v-btn name="submit-btn" @click="submitPost">Create</v-btn>
      <v-btn name="submit-btn" @click="clickCancel">Cancel</v-btn>
    </v-form>
  </div>
</template>

<script>
import validations from '@/utils/validations'
export default {

  // name: 'IndexPage',
  data() {
    return {
      confirmData: {
        title: '',
        description: ''
      },
      valid: false,
      ...validations
    }
  },
  methods: {
    loginUser() {
      
    },
    clickCancel() {
      this.$router.push('/post/post-create');
    },
    async submitPost() {
      let postData = { title: '', description: '', 
                      created_at: new Date().toISOString()}
      postData.title = this.$store.state.posts.title;
      postData.description = this.$store.state.posts.description;
      const userData = JSON.parse(localStorage.getItem('responseData'));
      postData.user = userData.id;
      postData.updated_user_id = userData.id;

      
      console.log(postData)
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in postData) {
        formData.append(data, postData[data]);
      }
      try {
        let response = this.$axios.$post(`/posts/`, formData, config);
        this.$router.push("/post/");
      } catch (e) {
        console.log(e);
      }
    },
  }
}
</script>

<style>
h1 {
  margin-bottom: 100px;
}
v-row {
  margin-bottom: 30px;
}
</style>