<template>
    <div v-if="comments.length > 0">
        <transition-group name="com-list">
            <comment-item 
                v-for="comment in comments" 
                :comment="comment"
                :curuser="curuser"
                :key="comment.id"
                @remove="$emit('remove', comment)"
            />
        </transition-group>

    </div>
    <div v-else>
        Комментариев ещё нет
    </div>
</template>

<script>
import CommentItem from '@/components/CommentItem';
export default {
    components: { CommentItem },
    props: {
        comments: {
            type: Array,
            required: true 
        },
        curuser: String,
    },
}
</script>

<style scoped>
.comment-list-item {
  display: inline-block;
  margin-right: 10px;
}
.comment-list-enter-active,
.comment-list-leave-active {
  transition: all 0.4s ease;
}
.comment-list-enter-from,
.comment-list-leave-to {
  opacity: 0;
  transform: translateX(130px);
}
.comment-list-move {
  transition: transform 0.4s ease;
}
</style>