#See https://aka.ms/customizecontainer to learn how to customize your debug container and how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/runtime:6.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["WKTAAE.DPU.FinancialAllocation/src/WKTAAE.DPU.Allocation.ASF.Worker/WKTAAE.DPU.Allocation.ASF.Worker.csproj", "WKTAAE.DPU.FinancialAllocation/src/WKTAAE.DPU.Allocation.ASF.Worker/"]
RUN dotnet restore "WKTAAE.DPU.FinancialAllocation/src/WKTAAE.DPU.Allocation.ASF.Worker/WKTAAE.DPU.Allocation.ASF.Worker.csproj"
COPY . .
WORKDIR "/src/WKTAAE.DPU.FinancialAllocation/src/WKTAAE.DPU.Allocation.ASF.Worker"
RUN dotnet build "WKTAAE.DPU.Allocation.ASF.Worker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "WKTAAE.DPU.Allocation.ASF.Worker.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "WKTAAE.DPU.Allocation.ASF.Worker.dll"]