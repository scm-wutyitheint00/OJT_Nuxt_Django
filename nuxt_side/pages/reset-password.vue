<template>
  <div class="register-page">
    <h1>Reset Password Form</h1>
    <v-container>
      <v-layout align-center justify-center>
        <v-flex sm7>
          <v-form v-model="isFormValid" ref="form">
            <v-text-field v-model="userData.password" label="New Password"
              :rules="[required('password'), minLenght('password', 8)]" :append-icon="
                userData.showPassword ? 'mdi-eye' : 'mdi-eye-off'
              " :type="userData.showPassword ? 'text' : 'password'"
              @click:append="userData.showPassword = !userData.showPassword"></v-text-field>
            <v-text-field v-model="userData.confirmpwd" label="New Password Confirm"
              :rules="[required('password'), minLenght('password', 8)]" :append-icon="
                userData.showPassword2 ? 'mdi-eye' : 'mdi-eye-off'
              " :type="userData.showPassword2 ? 'text' : 'password'"
              @click:append="userData.showPassword2 = !userData.showPassword2"></v-text-field>
            <p class="red--text" v-if="!userData.valid">{{ userData.error }}</p>
            <v-btn style="margin : 30px" :disabled="!isFormValid" @click="changePassword()">
              Submit
            </v-btn>
          </v-form>
        </v-flex>
      </v-layout>
      <v-dialog v-model="showDialog" persistent max-width="290">
        <v-card>
          <v-card-title><span class="text-subtitle-1 text--primary">{{ dialogMsg }}</span></v-card-title>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" text @click="clickOK()">
              OK
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
    async created() {
      const url = new URL(window.location.href);
      var code = url.searchParams.get("code");
      try {
        await this.$axios
          .$post(`/request-password?code=${code}`);
      } catch (err) {
        this.showDialog = true;
        this.dialogMsg = err.response.data;
      }
    },
  
    data: () => ({
      userData: {
        id: '',
        email: '',
        password: '',
        confirmpwd: '',
        showPassword: false,
        showPassword2: false,
        valid: true,
        error: null,
        type: ''
      },
      showDialog: false,
      dialogMsg: '',
      isFormValid: false,
      ...validations
    }),
    methods: {
      async createUser(userData) {
        userData.name = this.name;
        userData.type = userData.type === 'Admin' ? 1 : 2;
        userData.created_at = new Date().toISOString();
        userData.updated_at = new Date().toISOString();
        const config = {
          headers: { "content-type": "multipart/form-data" }
        };
        let formData = new FormData();
        for (let data in userData) {
          formData.append(data, userData[data]);
        }
        await this.$axios.$post(`/users/`, formData, config);
      },
      async changePassword() {
        if (this.userData.password !== this.userData.confirmpwd) {
          this.userData.error = "Password does not match!";
          this.userData.valid = false
        } else {
          this.userData.valid = true;
          this.userData.error = '';
          const url = new URL(window.location.href);
          var code = url.searchParams.get("code");
          try {
            await this.$axios
              .$post(`/reset-password?code=${code}&password=${this.userData.password}`)
              .then(data => {
                if (data) {
                  this.showDialog = true;
                  this.dialogMsg = data;
                }
              })
          } catch (err) {
            this.showDialog = true;
            this.dialogMsg = err.response.data;
          }
        }
      },
      clickOK() {
        this.$router.push('/');
      }
    },
  }
  </script>