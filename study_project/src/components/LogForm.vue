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
        <my-button 
            style="align-self: flex-end;
                   margin-top: 15px"
            @click="logUser"
        >
            Войти
        </my-button>
        <div v-if="logstat === 2">
            Неверное имя пользователя
        </div>
        <div v-if="logstat === 3">
            Неверный пароль
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
            logstat: 1,
        }
    },
    methods: {
        async logUser() {
            
            console.log({ author: this.user })
            const res = await axios.post('http://127.0.0.1:8000/api/authors/log/', { author: this.user });
            const out = res.data;
            if (out === "OK") {
                this.logstat = 1;
                this.$emit('log', this.user.name);
                this.user = {
                    name: '',
                    password: ''
                }
            }
            else if (out === "NoUser") {
                this.logstat = 2;
            }
            else if (out === "NoPass") {
                this.logstat = 3;
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
