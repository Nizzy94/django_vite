<template>
    <Base>
        <template #page_content="slotProps">
            <!-- <div class="q-px-lg"> -->
            <div
                class="q-mx-auto q-px-lg q-mt-lg"
                :class="{
                    'q-col-gutter-md row': $q.screen.gt.xs,
                    'column reverse mb-lg': $q.screen.lt.sm,
                }"
            >
                <div class="col-12 col-sm-4">
                    <q-separator v-if="$q.screen.lt.sm" spaced="16px" />
                    <!-- <q-separator :hidden="false" spaced="16px" /> -->
                    <div
                        class="flex justify-end"
                        :class="{ 'q-mt-lg': $q.screen.lt.sm }"
                    >
                        <ProfileSidebar />
                    </div>
                </div>
                <div class="col-12 col-sm-8">
                    <!-- <div class=""> -->
                    <slot name="form_content" :routes="slotProps.routes" />
                    <!-- </div> -->
                </div>
            </div>
            <!-- </div> -->
        </template>
    </Base>
</template>

<script setup>
import Base from "../../components/layouts/Base.vue";
import ProfileSidebar from "../../components/auth/ProfileSidebar.vue";
</script>

<style>
</style>