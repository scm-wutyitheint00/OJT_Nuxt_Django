<template>
  <div class="container">
    <h1 class="title">
      User Profile
    </h1>
    <v-row>
      <v-col cols="9">
        <v-form>
          <v-row>
            <v-col cols="2">
              <v-subtitle>Name</v-subtitle>
            </v-col>
            <v-col cols="8">
              <p class="text-subtitle"> {{  confirmData.name  }}
              </p>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="2">
              <v-subtitle>Email</v-subtitle>
            </v-col>
            <v-col cols="8">
              <p class="text-subtitle"> {{  confirmData.email  }}
              </p>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="2">
              <v-subtitle>Type</v-subtitle>
            </v-col>
            <v-col cols="8">
              <p class="text-subtitle">
                {{  confirmData.type  }}
              </p>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="2">
              <v-subtitle>Phone</v-subtitle>
            </v-col>
            <v-col cols="8">
              <p class="text-subtitle">{{  confirmData.phone  }}
              </p>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="2">
              <v-subtitle>Date of Birth</v-subtitle>
            </v-col>
            <v-col cols="8">
              <p class="text-subtitle">{{  confirmData.dob  }}
              </p>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="2">
              <v-subtitle>Address</v-subtitle>
            </v-col>
            <v-col cols="8">
              <p class="text-subtitle">
                {{  confirmData.address  }}
              </p>
            </v-col>
          </v-row>

          <nuxt-link :to="`/user/${confirmData.id}/edit`"><a href="#"><v-btn name="submit-btn">Edit</v-btn></a></nuxt-link>
          
        </v-form>
      </v-col>
      <v-col cols="3">
        <img v-if="url" :src="`${confirmData.profile}`" style="width: 100%;  float: left; margin-right: 10px;" />
      </v-col>
    </v-row>
  </div>
</template>
  
  <script>
import validations from '@/utils/validations'
export default {

  // name: 'IndexPage',
  data() {
    return {
      confirmData: {
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
        type: 1,
        phone: '',
        dob: '',
        profile: ''
      },
      url: '',
      valid: false,
      ...validations
    }
  },
  async created() {
    const loginMail = localStorage.getItem('loginEmail');
    await this.$axios.
      $get(`/users?email=${loginMail}`).then((data) => {
        if (data) {
          this.confirmData = data[0];
          this.url = this.confirmData.profile;
        }
      })
    console.log(this.confirmData)
  },
  methods: {
    loginUser() {
      console.log(this.confirmData)
    },
    clickCancel() {
      this.$router.push('/user/user-create');
    },
    async asyncData({ $axios, params }) {
      try {
        const loginMail = localStorage.getItem('loginEmail');
        let confirmData = await this.$axios.
          $get(`/users?email=${loginMail}`);
        console.log(confirmData)
        return { confirmData };
      } catch (e) {
        return { confirmData: [] };
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