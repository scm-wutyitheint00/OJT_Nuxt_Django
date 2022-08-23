<template>
  <div class="container">
    <h1 class="title">
      Confirm Post
    </h1>
    <v-form>
      <v-row>
        <v-col cols="2">
          <v-subheader>Title</v-subheader>
        </v-col>
        <v-col cols="8">
          <p class="text-subtitle-2" value="this.confirmData.title">
            {{ $store.state.posts.title }}
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subheader>Description</v-subheader>
        </v-col>
        <v-col cols="8">
          <p class="text-subtitle-2" value="this.confirmData.description">
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
      let postData = { title: '', description: '', updated_user_id: 1, 
                      created_at: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),}
      postData.title = this.$store.state.posts.title;
      postData.description = this.$store.state.posts.description;
      
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
</style>