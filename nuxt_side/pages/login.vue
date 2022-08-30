<template>
  <div>
    <h1>Login Form</h1>
    <v-container>
      <v-layout align-center justify-center>
        <v-flex sm7>
          <v-form>
            <v-text-field v-model="loginInfo.email" label="Enter your e-mail address" counter
              :rules="[required('email'), emailFormat()]"></v-text-field>
            <v-text-field v-model="loginInfo.password" label="Enter your password"
              :rules="[required('password'), minLenght('password', 8)]" :append-icon="
                loginInfo.showPassword ? 'mdi-eye' : 'mdi-eye-off'
              " :type="loginInfo.showPassword ? 'text' : 'password'" @click:append="
loginInfo.showPassword = !loginInfo.showPassword"></v-text-field>
            <v-layout justify-end>
              <a href="">Forgot Password</a>
            </v-layout>
            <p class="red--text" v-if="!loginInfo.valid">Invalid Email and Password!</p>
            <v-btn name="submit-btn" @click="loginUser(loginInfo)">Login</v-btn>
          </v-form>
        </v-flex>
      </v-layout>
    </v-container>

  </div>
</template>

<script>
import validations from '@/utils/validations'
export default {
  // name: 'IndexPage',

  data() {
    return {
      loginInfo: {
        email: '',
        password: '',
        valid: true,
        showPassword: false,
      },
      loginData: {
        logintime: '',
        token: ''
      },
      ...validations
    }
  },
  methods: {
    async isAdmin(mailData) {
      await this.$axios
        .$get(`/customuser/?search=${mailData}`)
        .then((response) => {
          if(response && response[0].type === 'Admin') {
            this.$store.commit('SET_MEMBER', false);
            localStorage.setItem("isMember", false);
          } else {
            this.$store.commit('SET_MEMBER', true);
            localStorage.setItem("isMember", true);
          }
          // this.$router.push('/');
        })
    },
    async loginUser(userData) {
      try {
        await this.$auth.loginWith('local', {
          data: userData,
        }).then(data => {
          console.log(data);
          // 
          localStorage.setItem('loginEmail', userData.email);

          localStorage.setItem("lastOperationDate", new Date().toString());
          this.$router.push('/post');
        });
        await this.isAdmin(userData.email);
      } catch (error) {
        this.loginInfo.valid = false;
      }
    },
  }
}
</script>

