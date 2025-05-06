const timeAt = document.getElementById('datetimepickerAt');
const timeTo = document.getElementById('datetimepickerTo');
const filter = new Filter();

if (timeAt && timeTo) {
  timeAt.addEventListener('change', () => {
    timeTo.min = timeAt.value;
  });
  timeTo.addEventListener('change', () => {
    timeAt.max = timeTo.value;
  });
}

const filterForm = document.getElementById('filterForm');
const filterChange = async (e) => {
    filter[e.target.name] = e.target.value;
    data = await filter.filter();

    document.getElementById('paymentsTableBody').innerHTML = "";
    data.forEach(payment => {
        document.getElementById('paymentsTableBody').innerHTML += payment;
    });
    
  
};
filterForm.addEventListener('change', filterChange);
