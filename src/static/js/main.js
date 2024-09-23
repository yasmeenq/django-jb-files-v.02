




function confirmDelete(event){
    const ok = confirm("Are u sure?")
    if(!ok) 
        event.preventDefault();
}