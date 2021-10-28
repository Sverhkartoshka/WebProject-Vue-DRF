<template>
    <form @submit.prevent>
        <my-input 
            v-model="user.name" 
            type="text" 
            placeholder="Логин"
        />
        <my-input 
            v-model="user.password" 
            type="password" 
            placeholder="Пароль"
        />
        <my-input 
            v-model="passcheck" 
            type="password" 
            placeholder="Повторите пароль"
        />
        <my-button 
            style="align-self: flex-end;
                   margin-top: 15px"
            @click="regUser"
        >
            Регистрация
        </my-button>
        <div v-if="message === 2">
            Пароли не совпадают
        </div>
        <div v-if="message === 3">
            Имя пользователя занято
        </div>
    </form>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            user: {
                name: '',
                password: ''
            },
            passcheck: '',
            message: 1,
        }
    },
    methods: {
        async regUser() {
            if (this.user.password == this.passcheck) {
                const res = await axios.post('http://127.0.0.1:8000/api/authors/reg/', { author: this.user });
                const out = res.data;
                if (out) {
                    this.message = 1;
                    this.$emit('log', this.user.name);
                    this.author = {
                        name: '',
                        password: ''
                    }
                }
                else {
                    this.message = 3;
                }
            }
            else {
                this.message = 2;
            }
        }
    },
}
</script>

<style scoped>
form {
    display: flex;
    flex-direction: column;
}
</style>
