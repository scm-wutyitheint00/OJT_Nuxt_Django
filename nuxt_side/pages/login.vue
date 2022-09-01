<template>
  <div>
    <h1>Login Form</h1>
    <v-container>
      <v-layout align-center justify-center>
        <v-flex sm7>
          <v-form v-model="isFormValid">
            <v-text-field v-model="loginInfo.email" label="Enter your e-mail address" counter
              :rules="[required('email'), emailFormat()]"></v-text-field>
            <v-text-field v-model="loginInfo.password" label="Enter your password"
              :rules="[required('password'), minLenght('password', 8)]" :append-icon="
              loginInfo.showPassword ? 'mdi-eye' : 'mdi-eye-off'" :type="loginInfo.showPassword ? 'text' : 'password'"
              @click:append="loginInfo.showPassword = !loginInfo.showPassword"></v-text-field>
            <v-layout justify-end>
              <a @click="forgetpwdDialog = true">Forgot Password</a>
            </v-layout>
            <p class="red--text" v-if="!loginInfo.valid">Invalid Email and Password!</p>
            <v-btn style="margin : 30px" :disabled="!isFormValid" name="submit-btn" @click="loginUser(loginInfo)">Login
            </v-btn>
          </v-form>
        </v-flex>
      </v-layout>
      <v-dialog v-model="forgetpwdDialog" persistent max-width="600px">
        <v-card>
          <v-card-title>
            <span class="text-h5">Forget Password Mail Send</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row justify="center">
                <v-col cols="10">
                  <v-text-field v-model="forgetPasswordMail" label="Enter your e-mail address" :rules="[required('email'), emailFormat()]">
                  </v-text-field>
                </v-col>
              </v-row>
              <v-row justify="center">
                <span v-if="!isMailSendMsg" class="subtitle-1">Password reset mail will be sent to your email.</span>
                <span v-if="isMailSendMsg && !pending" class="subtitle-1">{{isMailSend === true ? 'Password Reset mail has been sent..' : 'Email not found!'}}</span>
                <span v-if="isMailSendMsg && pending" class="subtitle-1">Mail is sending, please wait...</span>

              </v-row>
              <v-row justify="center">
                <v-btn :disabled="!forgetPasswordMail" style="margin-top : 30px" name="submit-btn" @click="forgetPasswordMailSend(forgetPasswordMail)">
                  Send
                </v-btn>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="forgetpwdDialog = false, forgetPasswordMail = '', isMailSendMsg=false">
              Close
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </div>
</template>

<script>
import validations from '@/utils/validations'
export default {
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
      isFormValid: false,
      forgetpwdDialog: false,
      forgetPasswordMail: '',
      isMailSend: false,
      isMailSendMsg: false,
      pending: false,
      ...validations
    }
  },
  methods: {
    async isAdmin(mailData) {
      await this.$axios
        .$get(`/users?email=${mailData}`)
        .then((response) => {
          localStorage.setItem('responseData', JSON.stringify(response[0]));
          if (response && response[0].type === "1") {
            this.$store.commit('SET_MEMBER', false);
            localStorage.setItem("isMember", false);
          } else {
            this.$store.commit('SET_MEMBER', true);
            localStorage.setItem("isMember", true);
          }
        })
      this.$router.push('/post');
    },
    async loginUser(userData) {
      try {
        await this.$auth.loginWith('local', {
          data: userData,
        }).then(data => {
          localStorage.setItem('loginEmail', userData.email);
          localStorage.setItem("lastOperationDate", new Date().toString());
        });
        await this.isAdmin(userData.email);
      } catch (error) {
        this.loginInfo.valid = false;
      }
    },
    async forgetPasswordMailSend(email) {
      this.isMailSendMsg = true;
      this.pending = true;
      await this.$axios
        .$get(`/mail?email=${email}`).then(data => {
          if(data === 'success') {
            this.isMailSend = true;
            this.pending = false;
          } else if( data === 'fail') {
            this.isMailSend = false;
            this.pending = false;
          }
        })
    }
  }
}
</script>

