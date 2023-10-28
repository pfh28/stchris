<template>
  <main>
    <div class="w-full h-5 bg-red-100 ">HELLOW?</div>

    <div v-for="treasure in treasureList" class="w-full h-5 bg-red-100 ">{{treasure.name}}</div>
  </main>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import TheWelcome from '../components/TheWelcome.vue'
import {useTreasureStore} from '../stores/treasureStore'

const treasureStore = useTreasureStore();

const {treasureList} = storeToRefs(treasureStore)

console.log(treasureList);

treasureStore.getTreasureList();

</script>