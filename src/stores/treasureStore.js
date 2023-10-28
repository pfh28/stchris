import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useTreasureStore = defineStore('treasureStore', () => {
    const treasureList = ref(null)
    //todo: does this need a paramater? I assume a user may access more than one list
    function getTreasureList() {
        treasureList.value = [
            {name: "a wheat penny", id: 1, description: "", points: 4, limit: 3},
            {name: "a Red fire Hydrant", id: 2, description: "", points: 2, limit: 1},
            {name: "a statue of Ben Franklin", id: 3, description: "", points: 4, limit: 1},
            {name: "an ice cream cone", id: 4, description: "", points: 4, limit: 1},
            {name: "A bicycle with parts missing", id: 5, description: "", points: 3, limit: 1}
        ]
    }
    return { treasureList, getTreasureList }
})