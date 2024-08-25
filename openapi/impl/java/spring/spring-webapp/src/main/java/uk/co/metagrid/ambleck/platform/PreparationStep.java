/*
 * <meta:header>
 *   <meta:licence>
 *     Copyright (C) 2024 University of Manchester.
 *
 *     This information is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, either version 3 of the License, or
 *     (at your option) any later version.
 *
 *     This information is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY; without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *   </meta:licence>
 * </meta:header>
 *
 *
 */
package uk.co.metagrid.ambleck.platform;

import java.util.UUID;

/**
 * Public interface representing a step needed to prepare an Execution session.
 *
 */
public interface PreparationStep<ParentType extends Execution>
    extends Runnable
    {
    public UUID getUuid();
    public ParentType getParent();

    public enum StateEnum
        {
        CREATED,
        RUNNING,
        COMPLETED,
        CANCELLED,
        FAILED
        }
    public StateEnum getState();

    /**
     * Public Runnable method.
     *
     */
    @Override
    public void run();

    /**
     * Start the step execution.
     *
     */
    public StateEnum start();

    /**
     * Complete the step execution.
     *
     */
    public StateEnum complete();

    /**
     * Cancel the step execution.
     *
     */
    public StateEnum cancel();

    /**
     * Fail the step execution.
     *
     */
    public StateEnum fail();

    }
