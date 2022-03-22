<template>
    <div class="column side_bar">
        <div class="bg-grey-4" style="height: 200px"></div>
        <div class="text-h6 q-mt-xl text-primary">Subscribe for update</div>
        <subscription-form :authUser="authUser" />
    </div>
</template>

<script setup>
import { toRefs } from "@vue/reactivity";
import SubscriptionForm from "./SubscriptionForm.vue";
const props = defineProps({
    authUser: {
        type: Object,
        default: {},
    },
});

const { authUser } = toRefs(props);
</script>

<style lang="sass">
.side_bar
    position: sticky
    top: 15px
</style>