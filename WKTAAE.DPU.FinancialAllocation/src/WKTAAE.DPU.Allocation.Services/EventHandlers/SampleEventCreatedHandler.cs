using MediatR;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using WKTAAE.DPU.Allocation.Contracts.Events;

namespace WKTAAE.DPU.Allocation.Services.EventHandlers
{
    public class SampleEventCreatedHandler : INotificationHandler<SampleEventCreated>
    {
        public SampleEventCreatedHandler()
        {
                
        }

        public async Task Handle(SampleEventCreated notification, CancellationToken cancellationToken)
        {
            // handle logic goes here
            throw new NotImplementedException();
        }
    }
}
