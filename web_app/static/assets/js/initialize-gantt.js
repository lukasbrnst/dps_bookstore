// let almostData =  document.getElementById("myData").innerHTML;
// let stringData = JSON.stringify(almostData);
// let data = JSON.parse(stringData);

//This could be an API call to grab data

// https://dev.to/ramonak/javascript-how-to-access-the-return-value-of-a-promise-object-1bck

// async refreshFunction() {
//   const result = await fetch('/api/v1', {method: 'GET'});
//   return result;
//   }

// async function refreshFunction() {
//   const result = await fetch("/api/v1", {
//     method: "GET",
//   });
//   return result.json();
// }

//   let data = await fetch("/api/v1")
//     .then((response) => {
//       return response.json();
//     })
//     .then((data) => {
//       console.log("GET response:");
//       console.log(data.data);
//       console.log(typeof(data.data))
//       return data.data;
//     })
//     .catch((err) => {
//       console.log(err);
//     });
//   // let mydata = await data.then((result) => result.data);
//   // console.log(mydata);
// }

// return finaldata

// let showData = () => {
//   finaldata.then((data) => {
//     console.log(data);
//     return data;
//   });
// };
// console.log(showData());
// let myveryfinaldata = showData();
// console.log("myveryfinaldata");
// console.log(myveryfinaldata);
// console.log(typeof myveryfinaldata);
// return myveryfinaldata;
// }

console.log("data", data);

const refreshFunction = () => {
  return data;
};

//Parameters that the chart expects
let params = {
  sidebarHeader: "Unused right now",
  noDataFoundMessage: "No data found",
  startTimeAlias: "start",
  endTimeAlias: "end",
  idAlias: "recordID",
  rowAlias: "row",
  linkAlias: null,
  tooltipAlias: "tooltip",
  groupBy: "groupId,subGroupId",
  groupByAlias: "group,subGroup",
  refreshFunction,
};

const chart = new Gantt("chart", params);
//Create the chart.
//On first render the chart will call its refreshData function on its own.
