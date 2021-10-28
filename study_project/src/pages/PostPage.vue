<template>
    <div>
        <my-input
            v-model="searchQuery"
            placeholder="Поиск..."
        />
        <div class="app__btns">
            <div v-if="activeUser === 'Anon'">
                <my-button @click="showLog">Вход</my-button>
                <my-button @click="showReg">Регистрация</my-button>
            </div>
            <my-button 
                @click="showPost"
                v-else
            >
                Создать пост
            </my-button>
            <my-select
                v-model="selectedSort"
                :options="sortOptions"
            />
        </div>
        <my-dialog v-model:show="dialogVisible">
            <post-form
                @create="createPost"
                v-if="dialogstat === 1"
                :curuser="activeUser"
            />
            <log-form
                @log="setUser"
                v-else-if="dialogstat === 2"
            />
            <reg-form
                @log="setUser"
                v-else-if="dialogstat === 3"
            />
        </my-dialog>
        <post-list 
            :posts="sortedAndSearchedPosts"
            :curuser="activeUser"
            @remove="removePost"
            @openpost="openPost"
            v-if="!isPostsLoading"
        />
        <div v-else>Идёт загрузка...</div>
        <div class="page__wrapper">
          <div
            v-for="pageNumber in totalPages"
            :key="pageNumber"
            class="page"
            :class="{
              'current-page': page === pageNumber
            }"
            @click="changePage(pageNumber)"
          >
            {{ pageNumber }}
          </div>
        </div>
    </div>
</template>

<script>
import PostForm from "@/components/PostForm";
import PostList from "@/components/PostList";
import MyButton from "@/components/UI/MyButton";
import MySelect from "@/components/UI/MySelect";
import MyInput from "@/components/UI/MyInput";
import axios from 'axios';
import LogForm from '@/components/LogForm';
import RegForm from '@/components/RegForm';

export default {
    components: {
        PostList, 
        PostForm,
        MyInput,
        MySelect,
        MyButton,
        LogForm,
        RegForm
    },
    props: {
        activeUser: String,
    },
    data() {
        return {
            posts: [],
            dialogVisible: false,
            isPostsLoading: false,
            selectedSort: '',
            searchQuery: '',
            page: 1,
            limit: 10,
            dialogstat: 1,
            totalPages: 1,
            sortOptions: [
                {value: 'title', name: 'По названию'},
                {value: 'description', name: 'По содержимому'},
            ],
        }
    },
    methods: {
        async fetchPosts() {
            this.isPostsLoading = true;
            try {
                setTimeout( async () => {
                    const response = await axios.get('http://127.0.0.1:8000/api/articles/', {
                        params: {
                            _page: this.page,
                            _limit: this.limit,
                        }
                    });
                    this.totalPages = Math.ceil(Object.keys(response.data.articles).length / this.limit);
                    this.posts = response.data.articles;
                }, 1000)
            } catch(e) {
                alert('Ошибка');
            } finally {
                this.isPostsLoading = false;
            }
        },
        async createPost(post) {
            const res = await axios.post('http://127.0.0.1:8000/api/articles/', { article: post });
            this.dialogVisible = false;
            this.fetchPosts();
        },
        async removePost(post) {
            const res = await axios.delete(`http://127.0.0.1:8000/api/articles/${encodeURIComponent(post.id)}`);
            this.fetchPosts();
        },
        setUser(user) {
            this.dialogVisible = false;
            this.$emit('logged', user);
        },
        showPost() {
            this.dialogstat = 1;
            this.dialogVisible = true;
        },
        showLog() {
            this.dialogstat = 2;
            this.dialogVisible = true;
        },
        showReg() {
            this.dialogstat = 3;
            this.dialogVisible = true;
        },
        changePage(pageNumber) {
            this.page = pageNumber
        },
        openPost(post) {
            this.$emit('openpost', post);
        },
        
    },
    mounted() {
        this.fetchPosts();
    },
    computed: {
        sortedPosts() {
            return [...this.posts].sort((post1, post2) => post1[this.selectedSort]?.localeCompare(post2[this.selectedSort])
            )
        },
        sortedAndSearchedPosts() {
            return this.sortedPosts.filter(post => post.title.toLowerCase().includes(this.searchQuery.toLowerCase()));
        }
    },
    watch: {
        page() {
            this.fetchPosts()
        }
    }
}
</script>

<style>
.app__btns {
    margin: 15px 0;
    display: flex;
    justify-content: space-between;
}
.page__wrapper {
    display: flex;
    margin-top: 15px;
    justify-content: center;
}
.page {
    border: 1px solid black;
    padding: 10px;
}
.current-page {
    border: 2px solid teal;
}
</style>